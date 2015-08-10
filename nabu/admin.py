# -*- coding:utf-8 -*-
from django import forms
from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.conf import settings
from django.forms.utils import ErrorList

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

    def render(self, name, value, attrs=None, choices=()):
        
        attrs['ng-model'] = "nabuGetterSetter"
        attrs['ng-model-options'] = "{ getterSetter: true }"
        attrs['ng-hide'] = "true"

        output = ''
        output += '<script>window.nabuData = \'%s\';</script>' % (value if value else '',)
        output += '<script>window.staticRoot = \'%s\';</script>' % (settings.STATIC_URL, )
        output += '<section ng-app="nabuAdmin">'
        output +=   '<div id="%s" ng-controller="nabuEditor">' % (name,)
        output +=       '<div nabu-form nabu-data="nabuData"></div>'
        output +=       super(PolymorphicWidget, self).render(name, value, attrs)
        output +=   '</div>'
        output += '</section>'
        return mark_safe(''.join(output))

class ActionForm(forms.ModelForm):

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None):
        super(ActionForm, self).__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance)
        self.fields['data'].widget = PolymorphicWidget()
    
    class Meta:
        model = Action
        fields = '__all__'
        exclude = ('counter', )
        #widgets = {
        #    'data': PolymorphicWidget(),
        #}

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):

    form = ActionForm

    class Media:
        css = {
            'all': ('css/nabu-admin.css',) 
        }
        js = ('https://ajax.googleapis.com/ajax/libs/angularjs/1.4.3/angular.min.js', 'js/nabu-django-admin.js')
