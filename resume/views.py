from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ExperiencePro, Formation
from .forms import ExperienceProForm, FormationForm


class ListExperienceProView(LoginRequiredMixin, ListView):
    model = ExperiencePro
    template_name = "experiences/experience_list.html"
    context_object_name = "experiences"


class CreateExperienceProView(LoginRequiredMixin, CreateView):
    model = ExperiencePro
    form_class = ExperienceProForm
    template_name = "experiences/experience_form.html"
    success_url = reverse_lazy("experiences-list")


class UpdateExperienceProView(LoginRequiredMixin, UpdateView):
    model = ExperiencePro
    form_class = ExperienceProForm
    template_name = "experiencepros/experiencepro_form.html"
    success_url = reverse_lazy("experiencepro-list")


class DeleteExperienceProView(LoginRequiredMixin, DeleteView):
    model = ExperiencePro
    template_name = "experiencepros/experiencepro_confirm_delete.html"
    success_url = reverse_lazy("experiencepro-list")


class ListFormationView(LoginRequiredMixin, ListView):
    model = Formation
    template_name = "formations/formations_list.html"
    context_object_name = "formations"


class CreateFormationView(LoginRequiredMixin, CreateView):
    model = Formation
    form_class = FormationForm
    template_name = "formations/formation_form.html"
    success_url = reverse_lazy("formations-list")


class UpdateFormationView(LoginRequiredMixin, UpdateView):
    model = Formation
    form_class = FormationForm
    template_name = "formations/formation_form.html"
    success_url = reverse_lazy("formations-list")


class DeleteFormationView(LoginRequiredMixin, DeleteView):
    model = Formation
    template_name = "formations/formation_confirm_delete.html"
    success_url = reverse_lazy("formations-list")