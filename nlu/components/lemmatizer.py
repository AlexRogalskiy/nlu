from nlu.pipe.pipe_component import SparkNLUComponent

class Lemmatizer(SparkNLUComponent):

    def __init__(self, annotator_class='lemmatizer', language='en', component_type='lemmatizer', get_default=False, model = None, nlp_ref='', nlu_ref ='', is_licensed=False, loaded_from_pretrained_pipe=False):

        if model != None : self.model = model
        else :
            if 'lemma' in annotator_class :
                from nlu import SparkNLPLemmatizer
                if get_default : self.model =  SparkNLPLemmatizer.get_default_model()
                else : self.model =  SparkNLPLemmatizer.get_pretrained_model(nlp_ref, language)
        SparkNLUComponent.__init__(self, annotator_class, component_type, loaded_from_pretrained_pipe=loaded_from_pretrained_pipe)
