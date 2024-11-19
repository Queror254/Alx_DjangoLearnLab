# Custom Permissions:

# - can_view: Permission to view a book.

# - can_create: Permission to create a new book.

# - can_edit: Permission to edit an existing book.

# - can_delete: Permission to delete a book.

# Groups:

# - Viewers: Can only view books.

# - Editors: Can view, create, and edit books.

# - Admins: Can view, create, edit, and delete books.

# Views:

# Each view has a permission check using the @permission_required decorator:

# - Only users with the corresponding permission can access the view.

# - If the user does not have the required permission, a 403 error will be raised.
