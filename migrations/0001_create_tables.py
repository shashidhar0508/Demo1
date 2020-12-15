from yoyo import step

steps = [
    step(
        "CREATE TABLE exam ( id serial NOT NULL, exam_name varchar(50) NOT NULL, "
        "question_count int4 NOT NULL,"
        "pass_percentage varchar(30) NOT NULL,"
        "created_on timestamp NOT NULL,"
        "created_by varchar(50) NOT NULL,"
        "updated_on timestamp NOT NULL,"
        "updated_by varchar(50) NOT NULL,"
        "CONSTRAINT pk_exam_id PRIMARY KEY (id))",
        "DROP TABLE exam"
    ),
    step(
        "CREATE TABLE technology ("
        "id serial NOT NULL,"
        "name varchar(150) NOT NULL,"
        "created_on timestamp NOT NULL,"
        "created_by varchar(50) NOT NULL,"
        "updated_on timestamp NOT NULL,"
        "updated_by varchar(50) NOT NULL,"
        "CONSTRAINT pk_technology_id PRIMARY KEY (id))"
    ),
    step(
        "CREATE TABLE questions ("
        "id serial NOT NULL,"
        "question_text varchar(150) NOT NULL,"
        "question_image varchar(150) NULL,"
        "question_level int4 NOT NULL,"
        "technology_id int4 NOT NULL,"
        "created_on timestamp NOT NULL,"
        "created_by varchar(50) NOT NULL,"
        "updated_on timestamp NOT NULL,"
        "updated_by varchar(50) NOT NULL,"
        "CONSTRAINT pk_questions_id PRIMARY KEY (id), "
        "CONSTRAINT fk_questions_technology_id foreign key(technology_id) references technology(id))"
    ),
    step(
        "CREATE TABLE options ("
        "id serial NOT NULL,"
        "option_text varchar(150) NOT NULL,"
        "correct_option int4 NOT NULL,"
        "question_id int4 NOT NULL,"
        "created_on timestamp NOT NULL,"
        "created_by varchar(50) NOT NULL,"
        "updated_on timestamp NOT NULL,"
        "updated_by varchar(50) NOT NULL,"
        "CONSTRAINT pk_options_id PRIMARY KEY (id),"
        "CONSTRAINT fk_options_question_id FOREIGN KEY (question_id)"
        "REFERENCES questions (id))"
    )
]
