use std::fs;

fn main() {
    let example = fs::read_to_string("../1.example").expect("File error");
    let result = solve_part_one(example.clone());
    println!("Part 1 - Example: {}", result); // 11
    let data = fs::read_to_string("../1.data").expect("File error");
    let result = solve_part_one(data.clone());
    println!("Part 1 - Real: {}", result); // 1603498

    let result = solve_part_two(example);
    println!("Part 2 - Example: {}", result); // 31
    let result = solve_part_two(data);
    println!("Part 2 - Real: {}", result); // 25574739
}

fn solve_part_one(contents: String) -> i32 {
    let lines = contents.trim().lines();
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();
    let mut total = 0;
    for line in lines {
        let items: Vec<&str> = line.split(" ").collect();
        left.push(items[0].parse().unwrap());
        right.push(items[3].parse().unwrap());
    }
    left.sort_unstable();
    right.sort_unstable();
    for (i, item) in left.iter().enumerate() {
        let result = (item - right[i]).abs();
        total += result;
    }
    return total;
}

fn solve_part_two(contents: String) -> i32 {
    let lines = contents.trim().lines();
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();
    let mut total = 0;
    for line in lines {
        let items: Vec<&str> = line.split(" ").collect();
        left.push(items[0].parse().unwrap());
        right.push(items[3].parse().unwrap());
    }
    for item in left.iter() {
        let count: i32 = right.iter().filter(|x| x == &item).count().try_into().unwrap();
        total += item * count;
    }
    return total;
}
