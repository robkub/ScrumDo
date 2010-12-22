from extras.interfaces import ScrumdoProjectExtra
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

import logging

class ExampleExtra( ScrumdoProjectExtra ):
  def getName(self):
    return "Example Extra"
    
  # Returns a version of the name consisting of only letters, numbers, or dashes
  def getSlug(self):
    return "example"

  def getLogo(self):
    return settings.STATIC_URL + "extras/example-logo.png"      
    
  # Returns a user-friendly description of this extra.  This text will be passed through a Markdown filter when displayed to the user.
  def getDescription(self):
    return "This Extra demonstrates the bare minimal required to get a ScrumDo Project based extra working."
    
  # Should return a django style response that handles any configuration that this extra may need.
  def doProjectConfigration( self, request, project ):
    return render_to_response("extras/example/configure.html", {
        "extra":self,
      }, context_instance=RequestContext(request)) 
    
  

  def associate( self, project):
    logging.info("Associated example extra with " + project.slug )


  def unassociate( self, project):
    logging.info("Unassociated example extra with " + project.slug )