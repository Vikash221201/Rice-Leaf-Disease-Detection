document.addEventListener("DOMContentLoaded", function () {
  const captureButton = document.getElementById("capture");
  const video = document.getElementById("video");
  const canvas = document.getElementById("canvas");
  const context = canvas.getContext("2d");
  const preview = document.getElementById("preview");
  let stream = null; // Store camera stream
  let isCameraOn = false; // Track camera state

  captureButton.addEventListener("click", function () {
      if (!isCameraOn) {
          // Open Camera
          navigator.mediaDevices.getUserMedia({ video: true })
              .then(function (mediaStream) {
                  stream = mediaStream;
                  video.srcObject = mediaStream;
                  video.style.display = "block";
                  captureButton.textContent = "Take Photo";
                  isCameraOn = true;
              })
              .catch(function (err) {
                  console.error("Error accessing camera:", err);
                  alert("Could not access the camera. Please allow camera permissions.");
              });
      } else {
          // Capture Image
          context.drawImage(video, 0, 0, canvas.width, canvas.height);

          // Stop camera
          if (stream) {
              stream.getTracks().forEach(track => track.stop());
          }
          video.style.display = "none";
          captureButton.textContent = "Capture Image";
          isCameraOn = false;

          // Show captured image
          preview.src = canvas.toDataURL("image/png");
      }
  });
});

// Image Preview for File Upload
function previewImage(event) {
  var reader = new FileReader();
  reader.onload = function () {
      var output = document.getElementById("preview");
      output.src = reader.result;
  };
  reader.readAsDataURL(event.target.files[0]);
}

// Show Loading & Redirect to Result Page
/*function predictDisease() {
  document.getElementById("loading").style.display = "block";
  setTimeout(() => {
      window.location.href = "result.html";
  }, 2000);
}*/



    
