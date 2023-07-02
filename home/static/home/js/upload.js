const userImage = document.querySelector(".user_image");
const overlay = document.querySelector(".overlay");
const deleteImage = document.querySelector(".delete-image");

// show delete button on hover
userImage.addEventListener("mouseover", () => {
  deleteImage.classList.add("show");
});

// hide delete button when mouse leaves the image
userImage.addEventListener("mouseout", () => {
  deleteImage.classList.remove("show");
});

// show delete confirmation when delete button is clicked
deleteImage.addEventListener("click", () => {
  const confirmDelete = confirm("Are you sure you want to delete this image?");
  if (confirmDelete) {
    userImage.src = "";
    overlay.style.display = "flex";
    deleteImage.classList.remove("show");
  }
});

// open file dialog when user clicks on overlay
overlay.addEventListener("click", () => {
  const input = document.createElement("input");
  input.type = "file";
  input.accept = "image/*";
  input.click();
  
  backsrc = userImage.src;
  
  input.addEventListener("change", (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => {
      userImage.src = reader.result;
      overlay.style.display = "none";
    };
  });
});
