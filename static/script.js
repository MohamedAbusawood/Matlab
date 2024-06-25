function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
}

// Toggle between file input and text area
function toggleFileInput() {
    var fileInput = document.getElementById('fileInput');
    if (fileInput.style.display === 'none') {
        fileInput.style.display = 'block';
        document.getElementById('textContent').style.display = 'none'; // Hide text area
    } else {
        fileInput.style.display = 'none';
        document.getElementById('textContent').style.display = 'block'; // Show text area
    }
}

// Read uploaded file and display its content in the text area
function uploadFile(event) {
    var fileInput = event.target;
    var file = fileInput.files[0];
    var reader = new FileReader();
    
    reader.onload = function(e) {
        document.getElementById('textContent').value = e.target.result;
    };
    
    reader.onerror = function(e) {
        console.error('Error reading the file.');
    };
    
    reader.readAsText(file);
}

// Download extracted keywords as a text file
function downloadKeywords() {
    var keywordsElements = document.querySelectorAll(".output-wrapper ul ");    
    var keywordsText = "";
    keywordsElements.forEach(function(element) {
        keywordsText += element.textContent.trim() + "\n";
    });

    var blob = new Blob([keywordsText], { type: "text/plain" });
    var link = document.createElement("a");
    link.download = "extracted_keywords.txt";
    link.href = window.URL.createObjectURL(blob);
    link.click();
}
