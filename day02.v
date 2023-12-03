import regex
import math { max }
import common as c

struct Game {
mut:
        id     int
        colors map[string]int
}

fn part_one(data string) int {
        games := parse_input(data)
        mut sum_ids := 0
        for g in games {
                if g.colors['red'] <= 12 && g.colors['green'] <= 13 && g.colors['blue'] <= 14 {
                        sum_ids += g.id
                }
        }
        return sum_ids
}

fn part_two(data string) int {
        games := parse_input(data)
        mut sum_powers := 0
        for g in games {
                sum_powers += g.colors['red'] * g.colors['green'] * g.colors['blue']
        }
        return sum_powers
}

fn parse_input(data string) []Game {
        mut games := []Game{}
        for line in data.split_into_lines() {
                games << parse_line(line)
        }
        return games
}

fn parse_line(line string) Game {
        query := r'Game ([0-9]+):((?: [\d]+ [\a]+,?)+;?)+'
        mut re := regex.regex_opt(query) or { panic(err) }
        re.group_csave_flag = true
        re.match_string(line)
        mut game := Game{}
        for cs_i := 1; cs_i < re.group_csave[0] * 3; cs_i += 3 {
                g_id := re.group_csave[cs_i]
                st := re.group_csave[cs_i + 1]
                en := re.group_csave[cs_i + 2]
                if g_id == 0 {
                        game.id = line[st..en].int()
                        continue
                }
                color_quantities := line[st..en].trim(' ;').split(',')
                for color_qty in color_quantities {
                        cq := color_qty.trim(' ').split(' ')
                        game.colors[cq[1]] = max(game.colors[cq[1]], cq[0].int())
                }
        }
        return game
}

fn main() {
        println(part_one(c.read_input(2)!))
        println(part_two(c.read_input(2)!))
}
