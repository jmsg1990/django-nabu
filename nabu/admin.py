# -*- coding:utf-8 -*-
from django import forms
from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.conf import settings

from .models import Ruleset, Rule, Action

class RuleInline(admin.StackedInline):
    model = Rule
    extra = 1


@admin.register(Ruleset)
class RulesetAdmin(admin.ModelAdmin):
    inlines = [
            RuleInline,
        ]
    exclude = ('rules', )


class PolymorphicWidget(forms.widgets.Textarea):

    def __init__(self, instance, **kwargs):
        print instance
        super(PolymorphicWidget, self).__init__(**kwargs)

    def render(self, name, value, attrs=None, choices=(), context={}):
        print attrs, context
        output = ''
        output += '<script>window.nabuData = \'%s\';</script>' % (value if value else '',)
        output += '<script>window.staticRoot = \'%s\';</script>' % (settings.STATIC_URL, )
        output += '<section ng-app="nabuAdmin">'
        output +=   '<div id="%s" ng-controller="nabuEditor"></div>' % (name,)
        output +=       '<div nabu-form></div>'
        output +=   '</div>'
        output += '</section>'
        return mark_safe(''.join(output))

class ActionForm(forms.ModelForm):

    def __init__(self, **kwargs):
        super(ActionForm, self).__init__(**kwargs)
        self.fields['data'].widget = PolymorphicWidget(kwargs.get('instance'))
    
    class Meta:
        model = Action
        fields = '__all__'
        #widgets = {
        #    'data': PolymorphicWidget(),
        #}

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):

    form = ActionForm

    class Media:
        css = {}
        js = ('https://ajax.googleapis.com/ajax/libs/angularjs/1.4.3/angular.min.js', 'js/nabu-django-admin.js')
