
// Check for the various File API support.
if (window.File && window.FileReader && window.FileList && window.Blob) {
  // Great success! All the File APIs are supported.
	alert('file api are present');
} else {
  alert('The File APIs are not fully supported in this browser.');
}
