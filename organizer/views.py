from django.http import HttpResponse
from .models import Composer, SetList, Piece, Sheet
from django.template.response import TemplateResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect

def redirect_index(request):
    return HttpResponseRedirect("/browse")

def index(request):
    context = {}
    return TemplateResponse(request, "organizer/index.html", context)

def search_composer(request, part_name):
    composers = Composer.objects.filter(name__icontains=part_name)
    pieces = Piece.objects.filter(name__icontains=part_name).order_by("name")
    print(pieces)
    if composers.count() + pieces.count() > 10: # kdo ví kolik je dobře...
        return JsonResponse({"error": "Příliš mnoho výsledků"})
    if composers.count() == 0 and pieces.count() == 0:
        return JsonResponse({"error": "Žádný výsledek"})
    return JsonResponse({
        "composers": [{"name":composer.name, "id":composer.id} for composer in composers],
        "pieces": [{"name":piece.name, "id":piece.id, "composers": [{"name": c.name, "id": c.id} for c in piece.composers.all()]} for piece in pieces]
        })

def composer_detail(request, composer_id):
    context = {"composer": Composer.objects.get(id=composer_id)}
    return TemplateResponse(request, "organizer/composer_detail.html", context)

def piece_detail(request, composer_id, piece_id):
    context = {"piece": Composer.objects.get(id=composer_id).piece_set.get(id=piece_id)}
    return TemplateResponse(request, "organizer/piece_detail.html", context)

def sheet_detail(request, composer_id, piece_id, sheet_id):
    sheet = Composer.objects.get(id=composer_id).piece_set.get(id=piece_id).sheet_set.get(id=sheet_id)
    return HttpResponseRedirect(sheet.file.url)


def draw(request):
    return TemplateResponse(request, "organizer/draw.html", {}) 

# setlists
def setlists(request):
    context = {
        "setlists": SetList.objects.all()
    }
    return TemplateResponse(request, "organizer/setlists.html", context)

def setlist_detail(request, setlist_id):
    context = {
        "setlist": SetList.objects.get(id=setlist_id),
        "relations": SetList.objects.get(id=setlist_id).setlistrelation_set.all()
    }
    print(len(context["relations"]))
    return TemplateResponse(request, "organizer/setlist_detail.html", context)

def setlist_relation_detail(request, setlist_id, relation_id):
    relace_all = SetList.objects.get(id=setlist_id).setlistrelation_set.order_by('numero')
    relace = relace_all.get(id=relation_id)
    c = 1
    for rel in relace_all:
        if rel == relace:
            real_numero = c
            break
        c += 1
    context = {
        "relation": relace,
        "real_numero": real_numero
    }
    return TemplateResponse(request, "organizer/setlist_relation_detail.html", context)

