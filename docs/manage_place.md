# 신규 맵/날씨 추가 시 작업

### place 테이블에 레코드 추가
	- id: 맵 인덱스 (하단에 기술된 PlaceName.py)
	- expansion: 
	- region
	- name_ko
	- name_en
	- category
	- isSpoiler
### services/weather.py에 데이터 추가
	- 신규 카테고리 추가가 필요한 경우 `region_category`에 추가
	- 인게임 지도 이미지에서 프로토 알파벳으로 표기되어 있는 경우 `unsundered`에 추가
		- 미탐사 해역 --> 해역 x 이동
		- 해역 x --> 해역 y 이동
		- 해역 y --> 해역 x 이동: 해당 건은 위 x --> y 케이스와 계산 값 자체는 동일하나, 빠른 계산을 위해 레코드를 추가하기 위함
### instance/weather_msg.py
	- 신규 날씨가 추가된 경우 날씨 딕셔너리에 한국어 string 추가
### 가상환경/EorzeaEnv/Data 폴더 내 각 파일 업데이트
	```
	작성일 기준 EorzeaEnv에 패치 7.38 (행성 파엔나)까지만 반영되어 있는 상태로, 이전 버전의 모듈을 일부 변형하여 사용하고 있음
	```	
	- PlaceName.py: 신규 맵 이름 및 날씨 인덱스 추가
	- TerritoryWeather.py: 신규 맵의 날씨 비율 매핑 추가
	- WeatherRate.py: 신규 맵 날씨 비율 추가
    	- WeatherRate.py 입력 방법:
			- tests/99_manual 내의 getRate.py로 날씨 예측 숫자 계산 (넉넉히 20~30개 정도)
			- 인게임 내 실제 날씨 변경 이력 기록
			- 숫자에 해당하는 날씨에 따라 날씨 비율표 기록 (※최소 5단위씩 변경되므로 경계값 제외 5단위만 관찰해도 충분함)
	- (신규 날씨가 추가되는 경우) Weather.py에 날씨 딕셔너리 추가