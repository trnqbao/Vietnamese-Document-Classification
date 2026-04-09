const API_URL = "http://127.0.0.1:8000/classify";

const btn = document.getElementById("classifyBtn");
const inputText = document.getElementById("inputText");
const result = document.getElementById("result");
const labelText = document.getElementById("labelText");
const confidenceBadge = document.getElementById("confidenceBadge");
const barFill = document.getElementById("barFill");
const confidenceLabel = document.getElementById("confidenceLabel");
const errorDiv = document.getElementById("error");

// Auto-fill selected text from active tab
chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
  chrome.scripting.executeScript(
    { target: { tabId: tabs[0].id }, func: () => window.getSelection().toString() },
    (results) => {
      if (results && results[0] && results[0].result) {
        inputText.value = results[0].result.trim();
      }
    }
  );
});

btn.addEventListener("click", async () => {
  const text = inputText.value.trim();
  if (!text) return;

  btn.disabled = true;
  btn.textContent = "Classifying...";
  result.style.display = "none";
  errorDiv.style.display = "none";

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    if (!res.ok) throw new Error(`Server error: ${res.status}`);

    const data = await res.json();
    const pct = (data.confidence * 100).toFixed(1);

    labelText.textContent = data.label;
    confidenceBadge.textContent = `${pct}%`;
    barFill.style.width = `${pct}%`;
    confidenceLabel.textContent = `Confidence: ${pct}%`;
    result.style.display = "block";
  } catch (err) {
    errorDiv.textContent = "Cannot connect to API. Make sure the server is running on port 8000.";
    errorDiv.style.display = "block";
  } finally {
    btn.disabled = false;
    btn.textContent = "Classify";
  }
});
