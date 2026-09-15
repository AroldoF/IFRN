fn identifier(string: &str) -> bool {
    let mut chars = string.chars();

    let Some(first) = chars.next() else {
        return false;
    };

    if !first.is_ascii_alphabetic() {
        return false;
    }

    if !chars.all(|c| c.is_ascii_alphanumeric()) {
        return false;
    }

    string.len() <= 6
}

fn main() {
    let string = "string";
    match identifier(string) {
        true => println!("{string} é Válida"),
        false => println!("{string} é Inválida")
    }
}

#[cfg(test)]
mod tests {
    use super::identifier;

    #[test]
    fn should_accept_valid_identifier() {
        // Arrange
        let input = "abc12";
        let expected = true;

        // Act
        let result = identifier(input);

        // Assert
        assert_eq!(result, expected);
    }

    #[test]
    fn should_reject_empty_identifier() {
        // Arrange
        let input = "";
        let expected = false;

        // Act
        let result = identifier(input);

        // Assert
        assert_eq!(result, expected);
    }

    #[test]
    fn should_accept_identifier_with_one_character() {
        // Arrange
        let input = "A";
        let expected = true;

        // Act
        let result = identifier(input);

        // Assert
        assert_eq!(result, expected);
    }

    #[test]
    fn should_accept_identifier_with_six_characters() {
        // Arrange
        let input = "abcdef";
        let expected = true;

        // Act
        let result = identifier(input);

        // Assert
        assert_eq!(result, expected);
    }

    #[test]
    fn should_reject_identifier_with_seven_characters() {
        // Arrange
        let input = "abcdefg";
        let expected = false;

        // Act
        let result = identifier(input);

        // Assert
        assert_eq!(result, expected);
    }

    #[test]
    fn should_reject_identifier_starting_with_digit() {
        // Arrange
        let input = "1abc";
        let expected = false;

        // Act
        let result = identifier(input);

        // Assert
        assert_eq!(result, expected);
    }

    #[test]
    fn should_reject_identifier_starting_with_special_character() {
        // Arrange
        let input = "_abc";
        let expected = false;

        // Act
        let result = identifier(input);

        // Assert
        assert_eq!(result, expected);
    }

    #[test]
    fn should_reject_identifier_containing_special_character() {
        // Arrange
        let input = "ab-c";
        let expected = false;

        // Act
        let result = identifier(input);

        // Assert
        assert_eq!(result, expected);
    }

    #[test]
    fn should_reject_identifier_containing_symbol() {
        // Arrange
        let input = "ab@1";
        let expected = false;

        // Act
        let result = identifier(input);

        // Assert
        assert_eq!(result, expected);
    }
}