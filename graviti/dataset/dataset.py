#!/usr/bin/env python3
#
# Copyright 2022 Graviti. Licensed under MIT License.
#

"""The implementation of the Graviti Dataset."""

from typing import Optional

from tensorbay.client.status import Status
from tensorbay.utility.user import UserMutableMapping

from graviti.client.dataset import get_dataset
from graviti.dataframe.frame import DataFrame
from graviti.manager.branch import BranchManager
from graviti.manager.commit import CommitManager
from graviti.manager.draft import DraftManager
from graviti.manager.tag import TagManager


class Dataset(UserMutableMapping[str, DataFrame]):
    """This class defines the basic concept of the dataset on Graviti.

    Arguments:
        access_key: User's access key.
        url: The URL of the graviti website.
        dataset_id: Dataset ID.
        name: The name of the dataset, unique for a user.
        status: The version control status of the dataset.
        alias: Dataset alias.

    """

    def __init__(
        self,
        access_key: str,
        url: str,
        dataset_id: str,
        name: str,
        *,
        status: Status,
        alias: str,
    ) -> None:
        self._access_key = access_key
        self._url = url
        self._dataset_id = dataset_id
        self._name = name
        self._status = status
        self._alias = alias
        self._is_public: Optional[bool] = None

    @property
    def access_key(self) -> str:
        """Return the access key of the user.

        Returns:
            The access key of the user.

        """
        return self._access_key

    @property
    def url(self) -> str:
        """Return the url of the graviti website.

        Returns:
            The url of the graviti website.

        """
        return self._url

    @property
    def dataset_id(self) -> str:
        """Return the ID of the dataset.

        Returns:
            The ID of the dataset.

        """
        return self._dataset_id

    @property
    def name(self) -> str:
        """Return the name of the dataset.

        Returns:
            The name of the dataset.

        """
        return self._name

    @property
    def status(self) -> Status:
        """Return the status of the dataset.

        Returns:
            The status of the dataset.

        """
        return self._status

    @property
    def alias(self) -> str:
        """Return the alias of the dataset.

        Returns:
            The alias of the dataset.

        """
        return self._alias

    @property
    def is_public(self) -> bool:
        """Return whether the dataset is public.

        Returns:
            Whether the dataset is public.

        """
        if self._is_public is None:
            info = get_dataset(url=self.url, access_key=self.access_key, dataset_id=self.dataset_id)
            self._is_public = info["isPublic"]
        return self._is_public

    @property
    def branches(self) -> BranchManager:
        """Get class :class:`~graviti.manager.dataset.BranchManager` instance.

        Return:
            Required :class:`~graviti.manager.dataset.BranchManager` instance.

        """

    @property
    def drafts(self) -> DraftManager:
        """Get class :class:`~graviti.manager.dataset.DraftManager` instance.

        Return:
            Required :class:`~graviti.manager.dataset.DraftManager` instance.

        """

    @property
    def commits(self) -> CommitManager:
        """Get class :class:`~graviti.manager.dataset.CommitManager` instance.

        Return:
            Required :class:`~graviti.manager.dataset.CommitManager` instance.

        """

    @property
    def tags(self) -> TagManager:
        """Get class :class:`~graviti.manager.dataset.TagManager` instance.

        Return:
            Required :class:`~graviti.manager.dataset.TagManager` instance.

        """

    def checkout(self, revision: str) -> None:
        """Checkout to a commit.

        Arguments:
            revision: The information to locate the specific commit, which can be the commit id,
                the branch, or the tag.

        """

    def checkout_draft(self, draft_number: int) -> None:
        """Checkout to a draft.

        Arguments:
            draft_number: The draft number.

        """

    def commit(self, title: str, description: str = "", *, tag: Optional[str] = None) -> None:
        """Commit the current draft.

        Arguments:
            title: The commit title.
            description: The commit description.
            tag: A tag for current commit.

        """

    def upload(
        self,
        jobs: int = 1,
    ) -> None:
        """Upload the local dataset to Graviti.

        Arguments:
            jobs: The number of the max workers in multi-thread upload.

        """

    def edit(self) -> None:
        """Edit the dataset."""