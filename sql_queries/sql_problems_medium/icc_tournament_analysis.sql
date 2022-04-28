-- Given a tournament result table create a summary report of total wins, total loss and total match played by a team in
-- icc tournament
--+--------+--------+--------+
--| team_1 | team_2 | winner |
--+--------+--------+--------+
--| India  | SL     | India  |
--| SL     | Aus    | Aus    |
--| SA     | Eng    | Eng    |
--| Eng    | NZ     | NZ     |
--| Aus    | India  | India  |
--+--------+--------+--------+

-- output
--+-------+------------+--------------+----------------------+
--| team  | total_wins | total_losses | total_matches_played |
--+-------+------------+--------------+----------------------+
--| India |          2 |            0 |                    2 |
--| SL    |          0 |            2 |                    2 |
--| SA    |          0 |            1 |                    1 |
--| Eng   |          1 |            1 |                    2 |
--| Aus   |          1 |            1 |                    2 |
--| NZ    |          1 |            0 |                    1 |
--+-------+------------+--------------+----------------------+

select team1 , count(*) as total_matches, count(winner) as total_wins, total_matches-total_wins as total_losses from icc groupby 1

create table icc_tournament_results (
	team_1 VARCHAR(10),
	team_2 VARCHAR(10),
	winner VARCHAR(10)
);


insert into icc_tournament_results values("India", "SL", "India");
insert into icc_tournament_results values("SL", "Aus", "Aus");
insert into icc_tournament_results values("SA", "Eng", "Eng");
insert into icc_tournament_results values("Eng", "NZ", "NZ");
insert into icc_tournament_results values("Aus", "India", "India");

select team, sum(win_count) as total_wins, sum(loss_count) as total_losses, count(1) as total_matches_played from (
	select team_1 as team,
		case when winner = team_1 then 1 else 0 end as win_count,
		case when winner != team_1 then 1 else 0 end as loss_count
	from icc_tournament_results
	union all
	select team_2 as team,
		case when winner = team_2 then 1 else 0 end as win_count,
		case when winner != team_2 then 1 else 0 end as loss_count
	from icc_tournament_results
) match_stats
group by team;