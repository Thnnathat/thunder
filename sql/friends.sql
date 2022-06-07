CREATE DATABASE test;


CREATE TABLE friends(
    id INT AUTO_INCREMENT,
    student_id VARCHAR(10),
    name VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    PRIMARY KEY (id)
);


INSERT INTO friends (student_id, name, first_name, last_name) 
VALUE 
('6440201561','เก่ง','ธนธัชย์','ชัยพุทธา'),
('6440200142','บีม','กัตติกา','ถวิล'),
('6440200696','แฮม','ชโณทิศ','ศรีษะ'),
('6440204334','บรีส','อรุณ','วันทอง'),
('6440204508','คิว','เอกศักดิ์','มะคำจั่น'),
('6440200373','เสือ','จตุรภูมิ','เสือประโคน');


SELECT * FROM friends WHERE student_id > (SELECT student_id FROM friends WHERE name = 'เก่ง');