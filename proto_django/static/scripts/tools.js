export function getCookieValue(name) {
    const regex = new RegExp(`(^| )${name}=([^;]+)`)
    const match = document.cookie.match(regex)
    if (match) {
        return match[2]
    }
}

export function showNotification(description) {
    let id = `base-toast-${document.querySelectorAll('#base-toast-container .toast').length + 1}`;
    let html_content = `<div id="${id}" class="toast align-items-center bg-secondary" role="alert" aria-live="assertive" \
            aria-atomic="true"> \
            <div class="d-flex"> \
                <div class="toast-body">${description}</div> \
                <button type="button" class="btn-close me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button> \
            </div> \
        </div>`;
    $(html_content)
        .appendTo('#base-toast-container');

    let html_item = document.getElementById(id);
    let toast = new bootstrap.Toast(html_item);

    html_item.addEventListener('hidden.bs.toast', () => {
        $('#' + id).remove();
    });
    toast.show();
}