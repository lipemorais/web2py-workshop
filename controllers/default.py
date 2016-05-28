# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

@auth.requires_login()
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hey Mundo!! Guenta eu que hoje eu to demais porque hoje encontrei a paz e a felicidade mora aqui.")
    return locals()

# @auth.requires(auth.has_membership('admin', auth.user.id))
@auth.requires_membership('admin')
def cadastrar_livros():
    form = crud.create(db.livros)
    # form = SQLFORM(db.livros)

    # if form.process().accepted:
    #     response.flash = 'Livro cadastrado com sucesso'
    # elif form.errors:
    #     response.flash = 'Deu merda, resolve ai' + str(form.errors)
    # else:
    #     response.flash = 'Deu merda!'
    #
    return locals()

@auth.requires_membership('admin')
def alterar_livros():
    response.flash = T("Alterar Livro")

    id_livro = request.args(0)

    # form = SQLFORM(db.livros, record=id_livro, deletable=True)
    form = crud.update(db.livros, id_livro)
    #
    # if form.process().accepted:
    #     response.flash = 'Livro alterado com sucesso'
    # elif form.errors:
    #     response.flash = 'Deu merda, resolve ai' + str(form.errors)
    # else:
    #     response.flash = 'Deu merda!'

    return locals()

@auth.requires_membership('admin')
def listar_livros():
    response.flash = T("Listar Livros")
    # livros = db(db.livros.id).select()

    livros = SQLFORM.grid(db.livros)

    return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
