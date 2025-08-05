import os
os.environ['SUPABASE_URL'] = 'http://localhost:8000'
os.environ['SUPABASE_KEY'] = 'dummy_key'
os.environ['GEMINI_API_KEY'] = 'dummy_key'

import unittest
from unittest.mock import patch, MagicMock
from app.services import profile_service
from app.models.user_model import UserProfile

class TestProfileService(unittest.TestCase):

    @patch('app.services.profile_service.supabase')
    def test_get_profile(self, mock_supabase):
        # Arrange
        mock_response = MagicMock()
        mock_response.data = {"id": 1, "full_name": "Maryanne Njenga"}
        mock_supabase.table.return_value.select.return_value.eq.return_value.single.return_value.execute.return_value = mock_response

        # Act
        profile = profile_service.get_profile()

        # Assert
        self.assertIsInstance(profile, UserProfile)
        self.assertEqual(profile.full_name, "Maryanne Njenga")

    @patch('app.services.profile_service.supabase')
    def test_update_profile(self, mock_supabase):
        # Arrange
        profile_data = UserProfile(full_name="Maryanne Njenga", email="maryanne@example.com")
        mock_response = MagicMock()
        mock_response.data = [profile_data.model_dump()]
        mock_supabase.table.return_value.update.return_value.eq.return_value.execute.return_value = mock_response

        # Act
        updated_profile = profile_service.update_profile(profile_data)

        # Assert
        mock_supabase.table.return_value.update.assert_called_with(profile_data.model_dump(exclude_unset=True))
        self.assertIsInstance(updated_profile, UserProfile)
        self.assertEqual(updated_profile.full_name, "Maryanne Njenga")
        self.assertEqual(updated_profile.email, "maryanne@example.com")

if __name__ == '__main__':
    unittest.main()
