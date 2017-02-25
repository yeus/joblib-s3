"""Helpers for easy registration of joblib store backends."""

from joblib import register_store_backend
from .s3fs_backend import S3FSStoreBackend
from .hdfs_backend import HDFSStoreBackend


def register_s3fs_store_backend():
    """Register a S3 store backend for joblib memory caching."""
    register_store_backend('s3', S3FSStoreBackend)


def register_hdfs_store_backend():
    """Register a HDFS store backend for joblib memory caching."""
    register_store_backend('hdfs', HDFSStoreBackend)
