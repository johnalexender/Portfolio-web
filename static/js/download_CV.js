function downloadResume() {
    const link = document.createElement("a");
    link.href = "/store/download-cv/"; // Use the defined URL path
    link.click();
  
    setTimeout(() => {
      alert("Successfully downloaded the document");
    }, 3500);
  }
  