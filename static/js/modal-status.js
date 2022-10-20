$(document).ready(function () {
  $("#modal-status").ready(function () {
    var status = $("input:hidden[name=modal-status]").val();
    if (status == "show") {
      var myModal = new bootstrap.Modal(document.getElementById("mainModal"));
      myModal.show();
    }
  });
});
