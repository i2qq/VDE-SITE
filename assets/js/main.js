document.addEventListener("DOMContentLoaded", () => {
  const tabWget = document.getElementById("tab-wget");
  const tabCurl = document.getElementById("tab-curl");
  const cmdText = document.getElementById("cmd-text");
  const copyBtn = document.getElementById("copy-btn");

  const cmds = {
    wget: "wget -qO- https://vde.vopple.uk/install.sh | sudo bash",
    curl: "curl -sSL https://vde.vopple.uk/install.sh | sudo bash"
  };

  let activeMode = "wget";

  if (tabWget && tabCurl && cmdText) {
    tabWget.addEventListener("click", () => {
      activeMode = "wget";
      tabWget.classList.add("active");
      tabCurl.classList.remove("active");
      cmdText.textContent = cmds.wget;
    });

    tabCurl.addEventListener("click", () => {
      activeMode = "curl";
      tabCurl.classList.add("active");
      tabWget.classList.remove("active");
      cmdText.textContent = cmds.curl;
    });
  }

  if (copyBtn && cmdText) {
    copyBtn.addEventListener("click", async () => {
      const textToCopy = cmdText.textContent.trim();
      try {
        await navigator.clipboard.writeText(textToCopy);
        copyBtn.classList.add("copied");
        copyBtn.innerHTML = `
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="20 6 9 17 4 12"></polyline>
          </svg>
          Copied!
        `;
        setTimeout(() => {
          copyBtn.classList.remove("copied");
          copyBtn.innerHTML = `
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
              <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
            </svg>
            Copy
          `;
        }, 2200);
      } catch (err) {
        console.error("Failed to copy command:", err);
      }
    });
  }
});
