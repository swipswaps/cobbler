import pytest

from api import CobblerAPI
from cobbler.actions.buildiso import BuildIso
from cobbler_collections.manager import CollectionManager
from items.distro import Distro


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

    def test_copy_boot_files(self):
        # Arrange
        buildiso = BuildIso(collection_manager)
        # TODO: Where to get fakefiles from again?
        testdistro = Distro(name="testdistro")
        # TODO: Where to put this?
        testdestdir = ""

        # Act
        buildiso.copy_boot_files(testdistro, testdestdir)

        # Assert
        assert False

    # TODO: Fill this with life
    @pytest.mark.parametrize("itemlist,listtype,expected_result", [
        ([], "system", []),
        ([], "profile", []),
        ([], "baditemtype", [])
    ])
    def test_filter_systems_or_profiles(self, itemlist, listtype, expected_result):
        # Arrange
        buildiso = BuildIso(collection_manager)

        # Act
        result = buildiso.filter_systems_or_profiles(itemlist, listtype)

        # Assert
        assert expected_result == result

    def test_generate_netboot_iso(self):
        # Arrange
        buildiso = BuildIso(collection_manager)

        # Act
        buildiso.generate_netboot_iso()

        # Assert
        assert False

    def test_generate_standalone_iso(self):
        # Arrange
        buildiso = BuildIso(collection_manager)

        # Act
        buildiso.generate_standalone_iso()

        # Assert
        assert False

    def test_run(self):
        # Arrange
        buildiso = BuildIso(collection_manager)

        # Act
        buildiso.run()

        # Assert
        assert False
