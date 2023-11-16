let deleteButtons = document.getElementsByClassName("btn-delete");
let editButtons = document.getElementsByClassName("btn-edit");
let deleteConfirm = document.getElementById("deleteConfirm");
let commentText = document.getElementById("form-ckeditor");
let formPlaceholder = document.getElementById("form-placeholder");
let commentForm = document.getElementById("commentForm");
let submitButton = document.getElementById("submitButton");

// empty the comment text after post
if (commentText) {
    commentText.value = "";
}


for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let deleteModal = new bootstrap.Modal(document.getElementById('deleteModalComment'));
        let commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        $(function () {
            document.querySelector('#form-ckeditor').scrollIntoView({
                behavior: 'smooth'
            });
        });
        commentText.classList.add("d-block");
        formPlaceholder.classList.add("d-none");
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
}