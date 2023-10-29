$(document).ready(function () {

  $(function () {
    $('[data-toggle="popover"]').popover()
  });

  $(".btn-outline-danger").on('click', function () {
    let deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    deleteModal.show();
  });

  setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
  }, 3000);

});
