from django.shortcuts import render, redirect
import psycopg2
import psycopg2.extras
from django.shortcuts import HttpResponse

# Create your views here.

def home_page(request):

        filtrar = request.GET.get('get_prioridad', default='%')
        with open("debug.log", "w") as debug_file:
            print(f"SELECT * FROM Nota WHERE prioridad LIKE '{filtrar}';", file=debug_file)
        if filtrar == 'todas':
            filtrar = '%'

        conn = psycopg2.connect(dbname="capitulo_6_db",
                                user="capitulo_6_user",
                                password="patata")

        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * FROM Nota WHERE prioridad LIKE '{filtrar}';")
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        params = {'notas': result}
        return render(request, 'formulario.html', params)


def anadir(request):
    titulo = request.POST['nombre_titulo']
    prioridad = request.POST['name_prioridad']
    contenido = request.POST['name_nota']

    conn = psycopg2.connect(dbname="capitulo_6_db",
                           user="capitulo_6_user",
                           password="patata")

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO nota VALUES ('{prioridad}', '{titulo}', '{contenido}');")
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(home_page)