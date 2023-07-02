const userImage = document.querySelector(".snoop_upload");

// open file dialog when user clicks on overlay
snoop_upload.addEventListener("click", () => {
    const input = document.createElement("input");
    input.type = "file";
    input.accept = "image/*";
    input.click();
    
    backsrc = snoopImage.src;
    
    input.addEventListener("change", (event) => {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => {
        snoopImage.src = reader.result;
        snoop_upload.style.display = "none";
      };
    });
  });