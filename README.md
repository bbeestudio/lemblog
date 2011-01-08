## Lemblog 1.0 beta

Lemblog - �������� ������, ���������� �� ���������� django � �������� �������� �����.

������������� ����������:
- ����
- �����������
- ���������������������
- ����� ������� �� ������� � �����
- RSS-�����
- ���������� �������� ��� �������
- ������� ������
- ����������� ��������� �������
- ��������� �����
- ���������� � �������
- ���������

� ����������:
- ����������� �����
- ��������� � ������������
- ����� ���� ���������� �����
- �������������� ������
- API ��� ���������� �������
- �����-������

� ������� ����� ������ ��������� �������:
- RSS (��������� RSS-�����)
- custom_user (���������� ����������� ������ ������������)
- menu (��������� ��������� ���� ����� ������ �����������������)
- twitter (����������� �������������� ���������� ���������� ������ � �������)
- counters (��������� ���� ��������� ���������)

���������� � ��:
Django 1.2 (�������� ������ �� 1.1) � ����
Python 2.5 � ����
Python Image Library

������ �������:
- ������� ������� aiden91@yandex.ru
- ��������� ����� igor.zapletnev@gmail.com

� ������ ����������� �������� ������� ������, �� �� ������ ������������ ����������� ���������� blog � templates. ������, ����������� ���������� ��������� (���� settings.py) ������� Django, ��� ��� � ��� ���������� �������������� ����.

## ��������� � ���������

1.  �������� �������� ���� lemblog 1.0 beta � ���������� �� � ���������� � django-���������.

2.  ��������� ���� ������

      DATABASES = {
			'default': {
            ...

            'django_dust',
		}
	}
	
	� ����� �������, ����� ������� ���� ������ sqlite3.
	
3.	������� � �������� ���������� �������� ���� � ���������� templates, ���������� � ����� �������. ���� ���������� ����� �� ����� templates � ���� ���������� ��������.

	TEMPLATE_DIRS = (
		...
	)
	
3.  ���� �� ����������� ���� ��, �� ��������� ������� `manage.py syncdb`. ���� �� �� ����������� �������� ��� ��������� �� ��������� ���� ������ (data.db), ����������� � ����� �������, �� ���������� ���� ���.

4.  ��������� ���������� ������ Django 'runserver 8000'.

	� settings.py ��������� ��������� ��� ������� �� ��������� ������� �� ����� 8000.

	
� ������ ����� ����� ��������� �������������� ������, ������� ���� �� ����������� ��� ������������ �� �������. ����� ��������� ������ � ��������� �� ������ �������� �� info@bbee.su

## ��������� ���������� � TWITTER

���� � ����� ����� �� ����������� ������������ ������� ���������� ���������� ������ � Twitter, �� ��������� ��������� ����:
	
1. 	��������������� ���� ���� �� http://dev.twitter.com , �������� ����������� ����, � ������ � �������� Callback URL: ����_��������_���/twitter/return
		
		� �������, http://blog.bbeestudio.ru/twitter/return
		
2. ���������� �onsumer key � �onsumer secret, �������������� � 12, 13 ������� ����� lemblog\blog\plugins\twitter\utils.py 
	
3. ������������� ������

[1]: http://bbeestudio.ru/lemblog
[2]: http://www.pythonware.com/products/pil/
