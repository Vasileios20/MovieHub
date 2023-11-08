$(document).ready(function () {
  
  $(function () {
    $('[data-toggle="popover"]').popover()
  });

  $("deleteModal").on('click', function () {
    let deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    deleteModal.show();
  });

  $("#form-placeholder").on('click', function () {
    $("#form-placeholder").addClass("d-none");
    $("#form-ckeditor").addClass("d-block");

  });

  setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
  }, 3000);
});
