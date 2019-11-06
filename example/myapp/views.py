from django.http import JsonResponse

from .query import schema


def graphql_view(request):

    query = """
        query {
            articles(find: { cID: 2 }) {
                ID
                title
                category {
                    title
                    ID
                }
            }
        }
    """

    result = schema.execute(query)

    if result.errors:
        return JsonResponse({"errors": str(result.errors)})

    return JsonResponse({"query": result.data})
