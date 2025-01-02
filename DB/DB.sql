DROP DATABASE IF EXISTS praven;
CREATE DATABASE praven;

USE praven;

-- 게시판 테이블 생성
CREATE TABLE board (
    boardId INT AUTO_INCREMENT PRIMARY KEY,       -- AUTO_INCREMENT 수정
    category VARCHAR(100) NOT NULL,               -- category의 길이를 적절히 줄임
    title VARCHAR(255) NOT NULL,
    user VARCHAR(255) NOT NULL,
    contents TEXT NOT NULL,                       -- TEXT로 수정, 길이가 더 길어질 수 있음
    createTime DATETIME DEFAULT CURRENT_TIMESTAMP, -- createTime 데이터 타입과 기본값 설정
    views INT DEFAULT 0,
    likes INT DEFAULT 0
);

-- 댓글 테이블 생성
CREATE TABLE comment (
    commentId INT AUTO_INCREMENT PRIMARY KEY,    -- AUTO_INCREMENT 수정
    boardId INT NOT NULL,
    userId VARCHAR(255) NOT NULL,
    contents TEXT NOT NULL,                      -- TEXT로 수정
    createTime DATETIME DEFAULT CURRENT_TIMESTAMP, -- createTime 데이터 타입과 기본값 설정
    FOREIGN KEY (boardId) REFERENCES board(boardId) ON DELETE CASCADE
);
