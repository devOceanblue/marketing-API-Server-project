USE `buzzvil`;

DROP TABLE IF EXISTS `user`;
create table user
(
    user_id    int,
    country    VARCHAR(254) not null,
    gender     VARCHAR(50) not null,
    balance    int default 0 not null,
    created_at TIMESTAMP default CURRENT_TIMESTAMP,
    updated_at TIMESTAMP default CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    constraint user_pk
        primary key (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `ad_campaigns`;
create table ad_campaigns
(
    id             int auto_increment,
    name           VARCHAR(254)                        null,
    image_url      VARCHAR(254)                        null,
    landing_url    VARCHAR(254)                        null,
    weight         int                                 null,
    target_country VARCHAR(10)                         null,
    target_gender  VARCHAR(2)                          null,
    reward         int                                 null,
    created_at     TIMESTAMP default CURRENT_TIMESTAMP,
    updated_at     TIMESTAMP default CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_rewarded    boolean                             null,
    constraint ad_campaigns_pk
        primary key (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `reward`;
create table reward
(
    id         int auto_increment
        primary key,
    user_id    int                                 null,
    credit     int                                 null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    constraint reward_user_user_id_fk
        foreign key (user_id) references user (user_id)
)ENGINE=INNODB DEFAULT CHARSET=utf8;
