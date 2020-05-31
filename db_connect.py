import pymysql os
from dotenv import load_dotenv
load_dotenv()

# 클래스 선언
class DBConnect:
    # 생성자 선언
    def __init__(self):
        # MySQL DB와 연결을 위한 connect 인스턴스를 선언
        self.conn = pymysql.connect(host='localhost', port=3306, user=os.getenv('MYSQL_ID'), password=os.getenv('MYSQL_PASSWORD'), db='test', charset='utf8' )
        # 파이썬에서 쿼리를 사용하고 저장하기 위한 cursor 인스턴스 선언
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    # 간단한 insert 메서드 정의
    def insert(self, tag_dict):
        try:
            # insert 쿼리 작성
            sql = """insert into test_insta (tag) 
                     values (%s)"""
            for k, v in tag_dict:
                # insert 쿼리를 실행한다.
                self.curs.execute(sql, "{}({})".format(k, v))
            # DML문 완료 후 커밋
            self.conn.commit()    
        except Exception as e:
            print(e)
        finally:
        # 커넥트 인스턴스를 닫아준다.
            self.conn.close()