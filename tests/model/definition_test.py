from src.openral_py.model.definition import Definition


class TestDefinition:

    def test_to_map_with_data(self):
        # Arrange
        definition_text = 'a test definition'
        definition_url = 'https://example.com'
        d = Definition(definition_text, definition_url)

        # Act
        result = d.to_map()

        # Assert
        assert result == {'definitionText': definition_text, 'definitionURL': definition_url}

    def test_to_map_without_data(self):
        # Arrange
        d = Definition()

        # Act
        result = d.to_map()

        # Assert
        assert result == {'definitionText': None, 'definitionURL': None}