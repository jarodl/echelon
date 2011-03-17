# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('echelon_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('desc', self.gf('django.db.models.fields.TextField')(max_length=140, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['echelon.Category'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=155)),
            ('hide_content', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hide_links', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('echelon', ['Category'])

        # Adding model 'Page'
        db.create_table('echelon_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=140)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('script', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('echelon', ['Page'])

        # Adding M2M table for field categories on 'Page'
        db.create_table('echelon_page_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm['echelon.page'], null=False)),
            ('category', models.ForeignKey(orm['echelon.category'], null=False))
        ))
        db.create_unique('echelon_page_categories', ['page_id', 'category_id'])

        # Adding model 'SiteSettings'
        db.create_table('echelon_sitesettings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('global_javascript', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('echelon', ['SiteSettings'])

        # Adding model 'SiteVariable'
        db.create_table('echelon_sitevariable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('value', self.gf('django.db.models.fields.TextField')()),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['echelon.SiteSettings'])),
        ))
        db.send_create_signal('echelon', ['SiteVariable'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('echelon_category')

        # Deleting model 'Page'
        db.delete_table('echelon_page')

        # Removing M2M table for field categories on 'Page'
        db.delete_table('echelon_page_categories')

        # Deleting model 'SiteSettings'
        db.delete_table('echelon_sitesettings')

        # Deleting model 'SiteVariable'
        db.delete_table('echelon_sitevariable')


    models = {
        'echelon.category': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Category'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'max_length': '140', 'blank': 'True'}),
            'hide_content': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hide_links': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['echelon.Category']", 'null': 'True', 'blank': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '155'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'echelon.page': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Page'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['echelon.Category']", 'symmetrical': 'False'}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '140'}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'script': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'echelon.sitesettings': {
            'Meta': {'object_name': 'SiteSettings'},
            'global_javascript': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'echelon.sitevariable': {
            'Meta': {'object_name': 'SiteVariable'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['echelon.SiteSettings']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['echelon']
