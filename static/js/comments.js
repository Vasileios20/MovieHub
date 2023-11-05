const deleteModal = new bootstrap.Modal(document.getElementById("deleteModalComment"));
let deleteButtons = document.getElementsByClassName("btn-delete");
let editButtons = document.getElementsByClassName("btn-edit");
let deleteConfirm = document.getElementById("deleteConfirm");
let commentText = document.getElementById("form-ckeditor");
let formPlaceholder = document.getElementById("form-placeholder");
let commentForm = document.getElementById("commentForm");
let submitButton = document.getElementById("submitButton");

// empty the comment text after post

commentText.value = "";


for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        window.scrollTo(0, 350);
        $(function() {      
            let isMobile = window.matchMedia("only screen and (max-width: 760px)").matches;
            if (isMobile) {
                window.scrollTo(0, 600);
            }
         });
        commentText.classList.add("d-block");
        formPlaceholder.classList.add("d-none");
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
}