"""
Model exported as python.
Name : ¸ðµ¨
Group : 
With QGIS : 32804
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing


class (QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        pass

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
        results = {}
        outputs = {}

        # ¹öÆÛ
        alg_params = {
            'DISSOLVE': False,
            'DISTANCE': 500,
            'END_CAP_STYLE': 0,  # µÕ±Û°Ô
            'INPUT': 'C:/Users/thlee/OneDrive - gaia3d.com/2024/edu4junior/data/subway_pt_part.gpkg',
            'JOIN_STYLE': 0,  # µÕ±Û°Ô
            'MITER_LIMIT': 2,
            'OUTPUT': 'TEMPORARY_OUTPUT',
            'SEGMENTS': 5,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs[''] = processing.run('native:buffer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return '¸ðµ¨'

    def displayName(self):
        return '¸ðµ¨'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return ()
