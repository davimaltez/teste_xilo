from django.contrib.admin import AdminSite


class VeredasAdminSite(AdminSite):
    def get_app_list(self, request, app_label=None):
        apps = super().get_app_list(request, app_label)
        nomes = {
            'Produto': 'Produtos',
            'VariacaoProduto': 'Estoque por tamanho',
            'Colecao': 'Coleções',
            'Categoria': 'Categorias',
        }
        ordem = {nome: indice for indice, nome in enumerate(nomes)}
        for app in apps:
            if app['app_label'] == 'loja':
                app['name'] = 'Gestão da loja'
                app['models'] = [
                    model for model in app['models']
                    if model['object_name'] != 'ImagemProduto'
                ]
                for model in app['models']:
                    model['name'] = nomes.get(model['object_name'], model['name'])
                app['models'].sort(key=lambda model: ordem.get(model['object_name'], len(ordem)))
            elif app['app_label'] == 'auth':
                app['name'] = 'Usuários e permissões'
        return sorted(apps, key=lambda app: app['app_label'] != 'loja')
