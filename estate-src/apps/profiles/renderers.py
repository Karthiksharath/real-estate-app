
import json

from rest_framework.renderers import JSONRenderer



class ProfileJsonRenderer(JSONRenderer):

  char_set = 'utf-8'

  def renderer(self, data, accepted_media_type = None, renderer_context = None):

    errors = data.get('errors',None)

    if errors is not None:

      return super(JSONRenderer, self).render(data)

    return json.dumps({'profile':data})




