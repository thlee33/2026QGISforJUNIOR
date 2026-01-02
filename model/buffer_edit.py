from qgis.core import QgsProcessing
import processing

# 버퍼 처리를 위한 매개변수 설정
alg_params = {
    'DISSOLVE': False,
    'DISTANCE': 500,
    'END_CAP_STYLE': 0,  # 둥글게
    'INPUT': 'C:/Users/thlee/OneDrive - gaia3d.com/2024/edu4junior/data/subway_pt_part.gpkg',  # 실제 레이어 경로
    'JOIN_STYLE': 0,  # 둥글게
    'MITER_LIMIT': 2,
    'SEGMENTS': 5,
    'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
}

# 버퍼 처리 실행
output = processing.run('native:buffer', alg_params)

# 결과 레이어 가져오기 (예: QGIS에 결과 레이어 추가)
result_layer = output['OUTPUT']
QgsProject.instance().addMapLayer(result_layer)
