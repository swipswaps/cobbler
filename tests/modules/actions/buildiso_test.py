import pytest

from cobbler.actions.buildiso import BuildIso
from cobbler.api import CobblerAPI
from cobbler.cobbler_collections.manager import CollectionManager
from cobbler.items.distro import Distro
from cobbler.items.profile import Profile
from cobbler.items.system import System


@pytest.fixture(scope="class")
def api():
    return CobblerAPI()


@pytest.fixture(scope="class")
def collection_manager(api):
    return CollectionManager(api=api)


class TestBuildiso:
    """Since BuildIso needs the collection manager and thus the api, as well as other information this test will
    require greater setup, although only this class shall be tested. Mocks are hard to program and we will try to
    avoid them.
    """

    @pytest.mark.parametrize("input_kopts_dict,exepcted_output", [
        ({}, "")
    ])
    def test_add_remaining_kopts(self, input_kopts_dict, exepcted_output):
        # Arrange (missing)
        # Act
        output = BuildIso.add_remaining_kopts(input_kopts_dict)

        # Assert
        assert output == exepcted_output

    def test_make_shorter(self, collection_manager):
        # Arrange
        buildiso = BuildIso(collection_manager)
        distroname = "Testdistro"

        # Act
        result = buildiso.make_shorter(distroname)

        # Assert
        assert type(result) == str
        assert distroname in buildiso.distmap
        assert result == "1"

    def test_copy_boot_files(self, collection_manager):
        # Arrange
        buildiso = BuildIso(collection_manager)
        # TODO: Where to get fakefiles from again?
        testdistro = Distro()
        testdistro.name = "testdistro"
        # TODO: Where to put this?
        testdestdir = ""

        # Act
        buildiso.copy_boot_files(testdistro, testdestdir)

        # Assert
        assert False

    # This test is done thrice due to the fact that parametrize and fixtures currently cannot be mixed.
    # For more see: https://github.com/pytest-dev/pytest/issues/349
    def test_filter_systems_or_profiles_system(self, collection_manager):
        # Arrange
        test_distro = Distro()
        test_distro.name = "testdistro"
        test_distro.kernel = ""
        test_distro.initrd = ""
        test_profile = Profile()
        test_profile.name = "testprofile"
        test_profile.distro = "testdistro"
        test_system = System()
        test_system.name = "testsystem"
        test_system.profile = "testprofile"
        collection_manager.api.add_distro(test_distro)
        collection_manager.api.add_profile(test_profile)
        collection_manager.api.add_system(test_system)
        itemlist = []
        buildiso = BuildIso(collection_manager)
        expected_result = []

        # Act
        result = buildiso.filter_systems_or_profiles(itemlist, "system")

        # Assert
        assert expected_result == result
        assert False

    # This test is done thrice due to the fact that parametrize and fixtures currently cannot be mixed.
    # For more see: https://github.com/pytest-dev/pytest/issues/349
    def test_filter_systems_or_profiles_profile(self, collection_manager):
        # Arrange
        itemlist = []
        buildiso = BuildIso(collection_manager)
        expected_result = []

        # Act
        result = buildiso.filter_systems_or_profiles(itemlist, "profile")

        # Assert
        assert expected_result == result
        assert False

    # This test is done thrice due to the fact that parametrize and fixtures currently cannot be mixed.
    # For more see: https://github.com/pytest-dev/pytest/issues/349
    def test_filter_systems_or_profiles_baditemtype(self, collection_manager):
        # Arrange
        buildiso = BuildIso(collection_manager)
        expected_result = []

        # Act
        result = buildiso.filter_systems_or_profiles([], "baditemtype")

        # Assert
        assert expected_result == result

    def test_generate_netboot_iso(self, collection_manager):
        # Arrange
        buildiso = BuildIso(collection_manager)

        # Act
        buildiso.generate_netboot_iso()

        # Assert
        assert False

    def test_generate_standalone_iso(self, collection_manager):
        # Arrange
        buildiso = BuildIso(collection_manager)

        # Act
        buildiso.generate_standalone_iso()

        # Assert
        assert False

    def test_run(self, collection_manager):
        # Arrange
        buildiso = BuildIso(collection_manager)

        # Act
        buildiso.run()

        # Assert
        assert False
