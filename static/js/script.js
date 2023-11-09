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

  $("#scroll-top-btn").on('click', function () {
    $(function () {
      document.body.scrollTop = 0; // For Safari
      document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    });
  });

  setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
  }, 3000);
});
