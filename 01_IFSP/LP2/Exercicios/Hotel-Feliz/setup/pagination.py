from flask import request
def paginate_or_all(query, to_dict=lambda x: x.to_dict()):
    """
    If `page` or `per_page` query params are present, return a dict with
    paginated items and metadata: { items, page, per_page, total, pages }.
    If neither param is present, return a plain list (backward compatible).
    Expects a SQLAlchemy BaseQuery supporting `.paginate()`.
    """
    page = request.args.get('page', type=int)
    per_page = request.args.get('per_page', type=int)
    if page is None and per_page is None:
        return [to_dict(item) for item in query.all()]
    if page is None:
        page = 1
    if per_page is None:
        per_page = 10
    pag = query.paginate(page=page, per_page=per_page, error_out=False)
    items = [to_dict(item) for item in pag.items]
    return {
        "items": items,
        "page": pag.page,
        "per_page": pag.per_page,
        "total": pag.total,
        "pages": pag.pages,
    }
