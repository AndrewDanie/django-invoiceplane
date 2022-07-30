function delete_current_table(t) {
    const parent = t.closest('.tablebox');
    parent.remove();
}