from django.test import TestCase
from django.urls import reverse, resolve
import job.views
import sujeito.views

# Create your tests here.
class JobsUrlTests(TestCase):

    def test_home_job_url_is_correct(self):
        url=reverse('job:homepage')
        self.assertEqual(url, '/')

    def test_login_url_is_correct(self):
        url = reverse('sujeito:login')
        self.assertEqual(url, '/login/')

    def test_logout_url_is_correct(self):
        url = reverse('sujeito:logout')
        self.assertEqual(url, '/logout/')

    def test_criar_usuario_url_is_correct(self):
        url = reverse('sujeito:usuario')
        self.assertEqual(url, '/usuario/')

    def test_cadastrarempresa_url_is_correct(self):
        url = reverse('sujeito:cadastrarempresa')
        self.assertEqual(url, '/cadastrarempresa/')

    def test_detalhe_job_url_is_correct(self):
        url= reverse('job:detalhe', args='1')
        self.assertEqual(url, "/jobs/1")

    def test_detalhe_vaga_empresa_url_is_correct(self):
        url= reverse('job:meuscandidatos', args='1')
        self.assertEqual(url, "/meuscandidatos/1")

    def test_criar_job_url_is_correct(self):
        url= reverse('sujeito:criarjob', args='1')
        self.assertEqual(url, "/criarjob/1")

    def test_dashboard_url_is_correct(self):
        url= reverse('sujeito:dashboard', args='1')
        self.assertEqual(url, "/dashboard/1")


class JobsViewsTests(TestCase):

    def test_homepage_view_is_correct(self):
        view= resolve(reverse('job:homepage'))
        self.assertIs(view.func.view_class, job.views.Homepage)


    def test_criar_usuario_view_is_correct(self):
        view= resolve(reverse('sujeito:usuario'))
        self.assertIs(view.func.view_class, sujeito.views.CriarPerfilUsuario)


    def test_cadastro_empresa_view_is_correct(self):
        view= resolve(reverse('sujeito:cadastrarempresa'))
        self.assertIs(view.func.view_class, sujeito.views.CriarNovaEmpresa)

    def test_criar_job_view_is_correct(self):
        view= resolve(reverse('sujeito:criarjob', args='1'))
        self.assertIs(view.func.view_class, sujeito.views.CriarJob)

    def test_detalhes_vaga_maisform_view_is_correct(self):
        view= resolve(reverse('job:detalhe', args='1'))
        self.assertIs(view.func.view_class, job.views.DetalheVagaCandidato)

    def test_detalhe_candidatos_aplicados_view_is_correct(self):
        view = resolve(reverse('job:meuscandidatos', args='1'))
        self.assertIs(view.func.view_class, job.views.DetalheVagaEmpresa)

    def test_detalhe_candidatos_aplicados_view_is_correct(self):
        view = resolve(reverse('sujeito:dashboard', args='1'))
        self.assertIs(view.func.view_class, sujeito.views.DashboardEmpresa)


