chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "classify-selection",
    title: "Classify selected text",
    contexts: ["selection"],
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "classify-selection") {
    chrome.action.openPopup();
  }
});
