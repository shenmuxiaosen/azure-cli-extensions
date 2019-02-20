# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .volume_reference import VolumeReference


class ApplicationScopedVolume(VolumeReference):
    """Describes a volume whose lifetime is scoped to the application's lifetime.

    :param name: Name of the volume being referenced.
    :type name: str
    :param read_only: The flag indicating whether the volume is read only.
     Default is 'false'.
    :type read_only: bool
    :param destination_path: The path within the container at which the volume
     should be mounted. Only valid path characters are allowed.
    :type destination_path: str
    :param creation_parameters: Describes parameters for creating
     application-scoped volumes.
    :type creation_parameters:
     ~azure.mgmt.servicefabricmesh.models.ApplicationScopedVolumeCreationParameters
    """

    _validation = {
        'name': {'required': True},
        'destination_path': {'required': True},
        'creation_parameters': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
        'destination_path': {'key': 'destinationPath', 'type': 'str'},
        'creation_parameters': {'key': 'creationParameters', 'type': 'ApplicationScopedVolumeCreationParameters'},
    }

    def __init__(self, name, destination_path, creation_parameters, read_only=None):
        super(ApplicationScopedVolume, self).__init__(name=name, read_only=read_only, destination_path=destination_path)
        self.creation_parameters = creation_parameters
