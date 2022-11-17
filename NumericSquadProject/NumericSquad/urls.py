"""NumericSquad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from numericApp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('notfound', views.notfound),

    #Interpolation
    path('vandermonde', views.vandermonde_ep),#, name="script_vandermonde"),
    path('lagrange', views.lagrange_ep),
    path('newton-interpolation', views.newton_interpolation_ep),
    path('splines', views.splines_ep),

    #Roots
    path('secant', views.secant_ep),
    path('incremental-search', views.incremental_search_ep),
    path('bisection', views.bisection_ep),
    path('newton-roots', views.newton_roots_ep),
    path('false-position', views.false_position_ep),
    path('fixedPoint', views.fixedPoint_ep),
    path('mulRT', views.mulRT_ep),
    path('muller', views.muller_ep),
    path('steffensen', views.steffensen_ep),
    path('aitken', views.aitken_ep),

    #Linear equations
    path('crout', views.crout_ep),
    path('jacobi', views.jacobi_ep),

    path('seidel',views.seidel_ep),
    path('sor',views.sor_ep),
    path('simple-lu', views.simple_LU_ep),
    path('partial-lu', views.partial_LU_ep),
    path('cholesky', views.cholesky_ep),
    path('doolittle',views.doolittle_ep)
]

urlpatterns += staticfiles_urlpatterns()

