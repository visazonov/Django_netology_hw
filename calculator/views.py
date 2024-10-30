from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def omlet_view(request):
    servings = int(request.GET.get('servings', 1))
    omlet = DATA['omlet']
    recipe = {}
    for k, v in omlet.items():
        recipe[k] = v * servings

    context = {
        'recipe' : recipe,
        'servings' : servings,
    }

    return render(request, 'calculator/index.html', context)


def pasta_view(request):
    servings = int(request.GET.get('servings', 1))
    pasta = DATA['pasta']
    recipe = {}
    for k, v in pasta.items():
        recipe[k] = v * servings

    context = {
        'recipe' : recipe,
        'servings' : servings,
    }

    return render(request, 'calculator/index.html', context)


def buter_view(request):
    servings = int(request.GET.get('servings', 1))
    buter = DATA['buter']
    recipe = {}
    for k, v in buter.items():
        recipe[k] = v * servings

    context = {
        'recipe' : recipe,
        'servings' : servings,
    }

    return render(request, 'calculator/index.html', context)

#omlet/?servings=4