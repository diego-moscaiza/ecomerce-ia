function loadVoiceflowChat() {
  const d = document;
  const t = "script";
  const v = d.createElement(t);
  const s = d.getElementsByTagName(t)[0];

  v.onload = function () {
    if (window.voiceflow) {
      window.voiceflow.chat.load({
        verify: { projectID: "665ab424f9872b3c9593002c" },
        url: "https://general-runtime.voiceflow.com",
        versionID: "production",
      });
    } else {
      console.error("Voiceflow no está disponible en window.");
    }
  };

  v.src = "https://cdn.voiceflow.com/widget/bundle.mjs";
  v.async = true;
  s.parentNode.insertBefore(v, s);
}

loadVoiceflowChat();
